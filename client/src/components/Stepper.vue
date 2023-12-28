<script>
export default {
    props: {
        datalists: Array,
        active: Number,
    }
}
</script>
<template>
    <div>
      <h2 class="sr-only">Steps</h2>
    
      <div
        class="relative after:absolute after:inset-x-0 after:top-1/2 after:block after:h-0.5 after:-translate-y-1/2 after:rounded-lg after:bg-gray-100"
      >
        <ol class="relative z-10 flex justify-between text-sm font-medium text-gray-500">
          <li v-for="data in datalists" :key="data.id" class="flex items-center gap-2 bg-white p-2">
            <span class="h-6 w-6 rounded-full text-center text-[10px]/6 font-bold" :class="data.id === active ? 'bg-zimored text-white' : 'bg-gray-100'">
              {{ data.id }}
            </span>
    
            <span class="hidden sm:block"> {{ data.name }} </span>
          </li>
        </ol>
      </div>
    </div>
  </template>