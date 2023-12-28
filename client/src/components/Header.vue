<script>
import { mapGetters } from 'vuex'
export default {
    name: 'Header',
    data(){
        return {

        }
    },
    computed: {
      ...mapGetters(['isLogin'])
    },
}
</script>
<template>
    <section class="bg-gray-50">
      <div class="mx-auto max-w-screen-xl px-4 py-32 lg:flex lg:h-screen lg:items-center">
        <div class="mx-auto max-w-xl text-center">
          <h1 class="text-3xl font-extrabold sm:text-5xl">
            Kuasai skill merancang
            <strong class="font-extrabold text-zimored sm:block"> Naikkan jam terbang dengan AI! </strong>
          </h1>
    
          <p class="mt-4 sm:text-xl/relaxed">
            Raih tingkat skill merancang desain anda menjadi tahap professional dengan banyak studi kasus dengan kecanggihan AI
          </p>
    
          <div class="mt-8 flex flex-wrap justify-center gap-4">
            <router-link
              class="block w-full rounded bg-zimored px-12 py-3 text-sm font-medium text-white shadow hover:bg-zimored focus:outline-none focus:ring active:bg-zimored sm:w-auto"
              :to="$store.getters.isLogin ? '/brief' : '/register'"
            >
              {{ $store.getters.isLogin ? 'Coba Brief Generator' : 'Daftar gratis' }}
            </router-link>
    
            <router-link
              class="block w-full rounded px-12 py-3 text-sm font-medium text-zimored shadow hover:text-zimored focus:outline-none focus:ring active:text-zimored sm:w-auto"
              :to="$store.getters.isLogin ? '/payment' : '#brief'"
            >
            {{ $store.getters.isLogin ? 'Lihat Harga' : 'Lihat Fitur' }}
            </router-link>
          </div>
        </div>
      </div>
    </section>
</template>