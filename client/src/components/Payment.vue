<script>
import { mapActions, mapMutations, mapState, useStore } from 'vuex';

export default {
    name: 'Payment Section',
    data(){
        return {
          ...mapState(['imgQris'])
        }
    },
    methods:{
      ...mapMutations(['lanjutStepPayment', 'resetStatePayment']),
      ...mapActions(['actionGetToken']),
      lanjut(){
        this.$store.commit('lanjutStepPayment', -1, true);
        this.$store.commit('resetStatePayment');
        this.$store.dispatch('actionGetToken');
      }
    },
    async setup(){
      const store = useStore();
      const data = await store.dispatch('actionPayment', {
        planId: store.state.activePlan + 1})
      return {data: data}
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
                :src="$store.state.imgQris"
                alt=""
                class="w-2/3 aspect-square rounded object-cover"
              />
        
            <div class="space-y-4 text-center">
          
              <span>Kode berlaku sampai dengan 30 menit</span>

            </div>

              <span
                @click="lanjut()"
                class="block rounded bg-gray-700 px-5 py-3 text-sm cursor-pointer text-gray-100 transition hover:bg-gray-600"
              >
                Sudah membayar
              </span>
        
            </div>
        </div>
    </div>
</template>