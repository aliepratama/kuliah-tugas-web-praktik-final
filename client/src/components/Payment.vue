<script>
export default {
    name: 'Payment Section',
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
        
          <div class="flex flex-col items-center mt-4 space-y-6">
            <img
                src="https://images.unsplash.com/photo-1618354691373-d851c5c3a990?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=830&q=80"
                alt=""
                class="w-2/3 aspect-square rounded object-cover"
              />
        
            <div class="space-y-4 text-center">
          
              <span>Kode berlaku sampai dengan 00:00</span>

            </div>

              <a
                href="#"
                class="block rounded bg-gray-700 px-5 py-3 text-sm text-gray-100 transition hover:bg-gray-600"
              >
                Sudah membayar
              </a>
        
            </div>
        </div>
    </div>
</template>