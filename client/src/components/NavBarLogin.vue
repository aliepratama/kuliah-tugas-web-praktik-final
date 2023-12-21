<script>
import { mapMutations, mapState } from 'vuex';

export default {
    name: 'NavBar Login',
    data(){
        return {
          
        }
    },
    methods: {
      ...mapMutations(['actionLogout']),
      logout(){
        this.$store.commit('actionLogout');
      }
    },
    computed: {
      ...mapState(['dataLogin']),
    }
}
</script>
<template>
  <header class="bg-gray-50">
    <div class="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 lg:px-8">
      <div class="flex items-center sm:justify-between sm:gap-4">
        <div class="flex flex-1 items-center justify-between gap-8 sm:justify-end">

          <router-link to="/brief">Brief Generator</router-link>

          <button type="button" class="group flex shrink-0 items-center rounded-lg transition">
            <span class="sr-only">Menu</span>
            <img
              alt="Man"
              src="https://images.unsplash.com/photo-1600486913747-55e5470d6f40?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80"
              class="h-10 w-10 rounded-full object-cover"
            />
  
            <p class="ms-2 hidden text-left text-xs sm:block">
              <strong class="block font-medium">{{ $store.state.dataLogin.user.firstName }}</strong>
  
              <span class="text-gray-500">{{ $store.state.dataLogin.user.email }}</span>
            </p>
  
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="ms-4 hidden h-5 w-5 text-gray-500 transition group-hover:text-gray-700 sm:block"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                clip-rule="evenodd"
              />
            </svg>
          </button>
          <button type="button" @click="logout()">Logout</button>
        </div>
      </div>
  
      <div class="mt-8">
        <h1 class="text-2xl font-bold text-gray-900 sm:text-3xl">Welcome Back, {{ $store.state.dataLogin.user.firstName }}!</h1>
  
        <p class="mt-1.5 text-sm text-gray-500">
          Your website has seen a 52% increase in traffic in the last month. Keep it up! 🚀
        </p>
      </div>
    </div>
  </header>
</template>