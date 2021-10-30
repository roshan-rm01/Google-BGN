<template>
      <div class='code-input-wrapper'>
        <input
          v-for="(cell, index) in cells"
          :key="cell.key"
          :ref="`code-input-${index}`"
          v-model.trim="cell.value"
          autocomplete="off"
          type="text"
          class="code-input"
          :maxlength="1"
          :style="`-webkit-text-security: ${cellsInputTypes[index]}`"
          @focus="focusedCellIndex = index"
          @keydown.delete="onCellErase(index, $event)"
          @paste="handlePasteEvent(index, $event)"
        />
      </div>
</template>

<script>
export default {
  props: {
    shouldMask: {
      default: false,
      type: Boolean,
    },
    length: {
      type: Number,
      default: 6,
    },
    errorMessages: {
      type: Array,
      default() {
        return []
      },
    },
    clear: {
      default: false,
      type: Boolean,
    },
  },
  data() {
    return {
      keyCode: null,
      elementValues: new Array(this.length),
      cells: [],
      cellsInputTypes: [],
      focusedCellIndex: 0,
      watchers: {},
    }
  },
  computed: {
    /**
     * Gets the individual cell values as a single string
     * @returns {String}
     * @example '123456'
     */
    getCodeInput() {
      return this.cells.reduce((result, cell) => result + cell.value, '')
    },
    /**
     * Gets input type to switch to after keypress
     * @returns {string}
     */
    getInputType() {
      return this.shouldMask ? 'disc' : 'none'
    },
  },
  watch: {
    /**
     * Handles the clear property changes and resets code input
     * @param value {Boolean}
     */
    clear(value) {
      if (value) {
        this.reset()
        this.$emit('update:clear', false)
      }
    },
    /**
     * Watches for changes to the codeInput and emits
     * @param value {String}
     * @example '123456'
     */
    getCodeInput(value) {
      this.$emit('input', value)
    },
    /**
     * Watches for changes in the value prop and fills each individual cell
     * @param value {String}
     */
    value(value) {
      if (value && this.length === value.length) {
        this.value.split('').forEach((cell, idx) => {
          this.cells[idx].value = cell || ''
        })
      } else {
        this.reset()
      }
    },
  },
  mounted() {
    this.initialiseCells()
    this.$nextTick(() => {
      this.focusCellByIndex()
    })
  },
  methods: {
    /**
     * Initialises all cells based on length
     */
    initialiseCells() {
      for (let key = 0; key < this.length; key += 1) {
        this.setCellObject(key)
        this.setCellInputType(key, 'tel')
        this.setCellWatcher(key)
      }
    },
    /**
     * Sets cell object with key
     * @param key {Number}
     */
    setCellObject(key) {
      this.$set(this.cells, key, { key, value: '' })
    },
    /**
     * Sets cell Watcher for a cell based on its Index
     * @param index {Number}
     */
    setCellWatcher(index) {
      const watchingProperty = `cells.${index}.value`
      this.watchers[watchingProperty] = this.$watch(
        watchingProperty,
        (newVal, oldVal) => this.onCellChanged(index, newVal, oldVal)
      )
    },
    /**
     * Handles left and right arrow key event
     * @param e {Event}
     */
    onKeyDown(e) {
      switch (e.keyCode) {
        /* left arrow key */
        case 37:
          this.focusPreviousCell()
          break
        /* right arrow key */
        case 39:
          this.focusNextCell()
          break
        default:
          break
      }
    },
    /**
     *  Maps focus to the previous Index
     */
    focusPreviousCell() {
      if (!this.focusedCellIndex) return

      this.focusCellByIndex(this.focusedCellIndex - 1)
    },
    /**
     *  Maps focus to the next Index
     */
    focusNextCell() {
      if (this.focusedCellIndex === this.length - 1) return

      this.focusCellByIndex(this.focusedCellIndex + 1)
    },
    /**
     *  Focuses on a cell based on the given index
     */
    focusCellByIndex(index = 0) {
      const ref = `code-input-${index}`
      const el = this.$refs[ref][0]
      this.$nextTick(() => {
        el.focus()
        el.select()
      })
      this.focusedCellIndex = index
    },
    /***
     * Updates cell input type and focuses on next cell
     */
    onCellChanged(index, newVal) {
      if (!this.isTheCellValid(newVal)) {
        this.cells[index].value = ''
        return
      }
      this.focusNextCell()
      setTimeout(this.setCellInputType, 200, index, this.getInputType)
    },
    /**
     * Updates cell input type given its index
     */
    setCellInputType(index, inputType) {
      this.$set(this.cellsInputTypes, index, inputType)
    },
    /**
     * checks if cell value is valid
     */
    isTheCellValid(cellValue) {
      if (!cellValue) {
        return false
      }
      return !isNaN(cellValue)
    },
    /**
     * Resets the state of the component
     */
    reset() {
      this.unwatchCells()
      this.initialiseCells()
      this.focusCellByIndex()
    },
    /**
     *  Clears the watchers object
     */
    unwatchCells() {
      const watchers = Object.keys(this.watchers)
      watchers.forEach((name) => this.watchers[name]())
    },
    /**
     * Clears cell value and focuses on previous cell
     */
    onCellErase(index, e) {
      this.cellsInputTypes[index] = 'tel'
      this.cells[index].value = ''
      this.focusPreviousCell()
      e.preventDefault()
    },
    /**
     * Handles On Paste Event and emits the pasted data if valid
     * @param index
     * @param event
     */
    handlePasteEvent(index, event) {
      if (index === 0) {
        const pasteData = (event.clipboardData || window.clipboardData).getData(
          'text'
        )
        if (pasteData.length === this.length && !isNaN(Number(pasteData))) {
          for (let i = 0; i < this.length; i += 1) {
            this.$nextTick(() => {
              this.cells[i].value = pasteData[i]
            })
          }
        }
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.code-input-wrapper {
  display: inline-flex;
}

.code-input {
  outline: none;
    max-width: 48px;
    height: 48px;
    text-align: center;
    font-weight: 500;
    font-size: 24px;
    line-height: 24px;
    letter-spacing: -0.384px;
    color: #383B46;
    background: #F7F8F9;
    border-radius: 6px;
    &:not(:first-child) {
      margin-left: 11px;
    }
  }
</style>
