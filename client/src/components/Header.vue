<script>
export default {
    name: 'Header',
    data(){
        return {

        }
    }
}
</script>
<template>
    <section class="bg-gray-50">
      <div class="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center">
        <div class="mx-auto max-w-xl text-center">
          <h1 class="text-3xl font-extrabold sm:text-5xl">
            Kuasai skill merancang
            <strong class="font-extrabold text-teal-600 sm:block"> Naikkan jam terbang dengan AI! </strong>
          </h1>
    
          <p class="mt-4 sm:text-xl/relaxed">
            Raih tingkat skill merancang desain anda menjadi tahap professional dengan banyak studi kasus dengan kecanggihan AI
          </p>
    
          <div class="mt-8 flex flex-wrap justify-center gap-4">
            <a
              class="block w-full rounded bg-teal-600 px-12 py-3 text-sm font-medium text-white shadow hover:bg-teal-600 focus:outline-none focus:ring active:bg-teal-600 sm:w-auto"
              href="/get-started"
            >
              Mulai sekarang
            </a>
    
            <a
              class="block w-full rounded px-12 py-3 text-sm font-medium text-teal-600 shadow hover:text-teal-600 focus:outline-none focus:ring active:text-teal-600 sm:w-auto"
              href="/about"
            >
              Lihat detail
            </a>
          </div>
        </div>
      </div>
    </section>
</template>