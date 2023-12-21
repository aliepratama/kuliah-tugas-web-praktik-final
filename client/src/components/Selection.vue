<script>
export default {
    props: {
        title: String,
        selection: Array,
    }
}
</script>
<template>
    <div>
      <label for="HeadlineAct" class="block text-sm font-medium text-gray-900"> {{ title }} </label>
    
      <select
        name="HeadlineAct"
        id="HeadlineAct"
        class="mt-1.5 w-full rounded-lg border-gray-300 text-gray-700 sm:text-sm"
      >
        <option value="">Silahkan pilih...</option>
        <option v-for="select in selection" :key="select" :value="select">{{ select }}</option>
      </select>
    </div>
  </template>