<script>
import { mapMutations } from 'vuex'

export default {
    name: 'Pricing Section',
    data(){
        return {
          
        }
    },
    methods: {
      ...mapMutations(['lanjutStepPayment']),
      pilihPaket(plan){
        this.$store.commit('lanjutStepPayment', plan)
      }
    },
}
</script>
<template>
    <div class="max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8 lg:py-16">
      <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 sm:items-stretch md:grid-cols-3 md:gap-8">
        <div class="divide-y divide-gray-200 rounded-2xl border border-gray-200 shadow-sm">
          <div class="p-6 sm:px-8">
            <h2 class="text-lg font-medium text-gray-900">
              Bronze
              <span class="sr-only">Plan</span>
            </h2>
    
            <p class="mt-2 text-gray-700">Paket yang cocok untuk mencoba hal baru.</p>
    
            <p class="mt-2 sm:mt-4">
              <strong class="text-3xl font-bold text-gray-900 sm:text-4xl"> Rp3.500 </strong>
    
              <span class="text-sm font-medium text-gray-700">/paket</span>
            </p>
    
            <span
              class="mt-4 block cursor-pointer rounded border border-zimored bg-zimored px-12 py-3 text-center text-sm font-medium text-white hover:bg-transparent hover:text-zimored focus:outline-none focus:ring active:text-zimored sm:mt-6"
              @click="pilihPaket(0)"
            >
              Beli paket
            </span>
          </div>
    
          <div class="p-6 sm:px-8">
            <p class="text-lg font-medium text-gray-900 sm:text-xl">Keuntungan:</p>
    
            <ul class="mt-2 space-y-2 sm:mt-4">
              <li class="flex items-center gap-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 text-green-500"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
    
                <span class="text-gray-700"> 5 Token </span>
              </li>
    
              <li class="flex items-center gap-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 text-green-500"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
    
                <span class="text-gray-700"> Respon dengan AI </span>
              </li>
    
              <li class="flex items-center gap-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 text-red-700"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
    
                <span class="text-gray-700"> Garansi respon AI </span>
              </li>
    
              <li class="flex items-center gap-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 text-red-700"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
    
                <span class="text-gray-700"> Customer support </span>
              </li>
    
              <li class="flex items-center gap-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 text-red-700"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
    
                <span class="text-gray-700"> Badge Eksklusif </span>
              </li>
            </ul>
          </div>
        </div>
    
        <div class="divide-y divide-gray-200 rounded-2xl border border-gray-200 shadow-sm">
          <div class="p-6 sm:px-8">
            <h2 class="text-lg font-medium text-gray-900">
              Silver
              <span class="sr-only">Plan</span>
            </h2>
    
            <p class="mt-2 text-gray-700">Paket untuk pengembangan skill yang hemat.</p>
    
            <p class="mt-2 sm:mt-4">
              <strong class="text-3xl font-bold text-gray-900 sm:text-4xl"> Rp5.000 </strong>
    
              <span class="text-sm font-medium text-gray-700">/paket</span>
            </p>
    
            <span
              class="mt-4 block cursor-pointer rounded border border-zimored bg-zimored px-12 py-3 text-center text-sm font-medium text-white hover:bg-transparent hover:text-zimored focus:outline-none focus:ring active:text-zimored sm:mt-6"
              @click="pilihPaket(1)"
            >
              Beli paket
            </span>
          </div>
    
          <div class="p-6 sm:px-8">
            <p class="text-lg font-medium text-gray-900 sm:text-xl">Keuntungan:</p>
    
            <ul class="mt-2 space-y-2 sm:mt-4">
              <li class="flex items-center gap-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 text-green-500"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
    
                <span class="text-gray-700"> 10 Token </span>
              </li>
    
              <li class="flex items-center gap-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 text-green-500"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
    
                <span class="text-gray-700"> Respon dengan AI </span>
              </li>
    
              <li class="flex items-center gap-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 text-green-500"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
    
                <span class="text-gray-700"> Garansi respon AI </span>
              </li>
    
              <li class="flex items-center gap-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 text-green-500"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
    
                <span class="text-gray-700"> Customer support </span>
              </li>
    
              <li class="flex items-center gap-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 text-red-700"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
    
                <span class="text-gray-700"> Badge Eksklusif </span>
              </li>
            </ul>
          </div>
        </div>
    
        <div class="divide-y divide-gray-200 rounded-2xl border border-gray-200 shadow-sm">
          <div class="p-6 sm:px-8">
            <h2 class="text-lg font-medium text-gray-900">
              Gold
              <span class="sr-only">Plan</span>
            </h2>
    
            <p class="mt-2 text-gray-700">Paket untuk kebutuhan sehari-hari.</p>
    
            <p class="mt-2 sm:mt-4">
              <strong class="text-3xl font-bold text-gray-900 sm:text-4xl"> Rp7.000 </strong>
    
              <span class="text-sm font-medium text-gray-700">/paket</span>
            </p>
    
            <span
              class="mt-4 block cursor-pointer rounded border border-zimored bg-zimored px-12 py-3 text-center text-sm font-medium text-white hover:bg-transparent hover:text-zimored focus:outline-none focus:ring active:text-zimored sm:mt-6"
              @click="pilihPaket(2)"
            >
              Beli paket
            </span>
          </div>
    
          <div class="p-6 sm:px-8">
            <p class="text-lg font-medium text-gray-900 sm:text-xl">Keuntungan:</p>
    
            <ul class="mt-2 space-y-2 sm:mt-4">
              <li class="flex items-center gap-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 text-green-500"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
    
                <span class="text-gray-700"> 15 Token </span>
              </li>
    
              <li class="flex items-center gap-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 text-green-500"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
    
                <span class="text-gray-700"> Respon dengan AI </span>
              </li>
    
              <li class="flex items-center gap-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 text-green-500"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
    
                <span class="text-gray-700"> Garansi respon AI </span>
              </li>
    
              <li class="flex items-center gap-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 text-green-500"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
    
                <span class="text-gray-700"> Customer support </span>
              </li>
    
              <li class="flex items-center gap-1">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="h-5 w-5 text-green-500"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                </svg>
    
                <span class="text-gray-700"> Badge Eksklusif </span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
</template>