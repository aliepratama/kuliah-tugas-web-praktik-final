<script>
export default {
    name: 'Checkout Section',
    data(){
        return {
          
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
          <button class="absolute end-4 top-4 text-gray-600 transition hover:scale-110">
            <span class="sr-only">Close cart</span>
        
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
            <ul class="space-y-4">
    
              <li class="flex items-center gap-4">
                <img
                  src="https://images.unsplash.com/photo-1618354691373-d851c5c3a990?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=830&q=80"
                  alt=""
                  class="h-16 w-16 rounded object-cover"
                />
        
                <div>
                  <h3 class="text-sm text-gray-900">Paket Bronze</h3>
        
                  <dl class="mt-0.5 space-y-px text-[10px] text-gray-600">
                    <div>
                      <dt class="inline">Jumlah token:</dt>
                      <dd class="inline">5</dd>
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
                <dd>Rp5000</dd>
              </div>

              <div class="flex justify-between">
                <dt>Pajak</dt>
                <dd>Rp500</dd>
              </div>

              <div class="flex justify-between">
                <dt>Diskon</dt>
                <dd>-Rp500</dd>
              </div>

              <div class="flex justify-between !text-base font-medium">
                <dt>Total</dt>
                <dd>Rp5000</dd>
              </div>
            </dl>

          </div>
        </div>

              <a
                href="#"
                class="block rounded bg-gray-700 px-5 py-3 text-sm text-gray-100 transition hover:bg-gray-600"
              >
                Bayar pakai QRIS
              </a>
        
            </div>
          </div>
        </div>
    </div>
</template>