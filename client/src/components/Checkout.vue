<script>
import { mapMutations, mapState } from 'vuex';
export default {
    name: 'Checkout Section',
    data(){
        return {
          ...mapState(['activePlan', 'pricelist']),
          data: this.$store.state.pricelist[this.$store.state.activePlan],
        }
    },
    methods: {
      ...mapMutations(['lanjutStepPayment', 'backStepPayment']),
      kembali(){
        this.$store.commit('backStepPayment', true);
      }
    },
}
</script>
<template>
    <div class="flex w-full justify-center py-16">
        <div
          class="relative w-screen max-w-sm bg-gray-100 px-4 py-8 sm:px-6 lg:px-8 rounded-md"
          aria-modal="true"
          role="dialog"
          tabindex="-1"
        >
          <button @click="kembali()" class="absolute end-4 top-4 text-gray-600 transition hover:scale-110">
            <span class="sr-only">Pembayaran</span>
        
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="h-5 w-5"
            >
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        
          <div class="mt-4 space-y-6">
            <ul>
    
              <li class="flex items-center">
                <div>
                  <h3 class="text-md font-bold text-zimored">Paket {{ data.name }}</h3>
        
                  <dl class="mt-0.5 space-y-px text-sm text-gray-600">
                    <div>
                      <dt class="inline">Jumlah token:</dt>
                      <dd class="inline">{{ data.token }}</dd>
                    </div>
        
                    <div>
                      <dt class="inline">Batas waktu:</dt>
                      <dd class="inline">selamanya</dd>
                    </div>
                  </dl>
                </div>
              </li>
    
            </ul>
        
            <div class="space-y-4 text-center">
                
                <div class="mt-8 flex justify-end border-t border-gray-100 pt-8">
          <div class="w-screen max-w-lg space-y-4">
            <dl class="space-y-0.5 text-sm text-gray-700">
              <div class="flex justify-between">
                <dt>Subtotal</dt>
                <dd>Rp{{ data.subtotal }}</dd>
              </div>

              <div class="flex justify-between">
                <dt>Pajak</dt>
                <dd>Rp{{ data.tax }}</dd>
              </div>

              <div class="flex justify-between">
                <dt>Diskon</dt>
                <dd>-Rp{{ data.discount }}</dd>
              </div>

              <div class="flex justify-between !text-base font-medium">
                <dt>Total</dt>
                <dd>Rp{{ data.total }}</dd>
              </div>
            </dl>

          </div>
        </div>

              <span
                @click="$store.commit('lanjutStepPayment')"
                class="block rounded bg-gray-700 px-5 py-3 text-sm cursor-pointer text-gray-100 transition hover:bg-gray-600"
              >
                Bayar pakai QRIS
              </span>
        
            </div>
          </div>
        </div>
    </div>
</template>