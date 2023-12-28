<script>
import { mapMutations, mapState } from 'vuex';
import 'flowbite';

export default {
    name: 'NavBar Login',
    props: {
      active: String,
    },
    data(){
        return {
          
        }
    },
    methods: {
      ...mapMutations(['actionLogout', 'actionGetToken']),
      logout(){
        this.$store.commit('actionLogout');
      }
    },
    computed: {
      ...mapState(['dataLogin']),
    },
    mounted(){
      this.$store.dispatch('actionGetToken')
    },
}
</script>
<template>
  <header class="bg-white">
      <div class="mx-auto max-w-screen-xl px-4 sm:px-6 lg:px-8">
        <div class="flex h-16 items-center justify-between">
          <div class="md:flex md:items-center md:gap-12">
            <router-link class="block text-zimored" to="/">
              <span class="sr-only">Home</span>
              <img class="h-8" src="../assets/color.webp" alt="Zimo Tools Logo">
            </router-link>
          </div>
    
          <div class="hidden md:block">
            <nav aria-label="Global">
              <ul class="flex items-center gap-6 text-sm">
                <li>
                  <router-link 
                  class="text-gray-500 transition hover:text-gray-500/75"
                  :class="active == 'brief' ? 'font-bold' : ''"
                  to="/brief"> Brief Generator </router-link>
                </li>
    
                <li>
                  <router-link 
                  class="text-gray-500 transition hover:text-gray-500/75"
                  :class="active == 'rater' ? 'font-bold' : ''"
                  to="/rater"> Design Rater </router-link>
                </li>
    
                <li>
                  <router-link 
                  class="text-gray-500 transition hover:text-gray-500/75"
                  :class="active == 'payment' ? 'font-bold' : ''"
                  to="/payment"> Pembayaran </router-link>
                </li>
    
                <li>
                  <router-link 
                  class="text-gray-500 transition hover:text-gray-500/75"
                  :class="active == 'history' ? 'font-bold' : ''"
                  to="/history"> Riwayat </router-link>
                </li>
    
              </ul>
            </nav>
          </div>
    
          <div class="sm:flex" id="dropdownHoverButton" data-dropdown-toggle="dropdownHover" data-dropdown-trigger="hover">
            <button type="button" class="group flex shrink-0 items-center rounded-lg transition">
              <span class="sr-only">Menu</span>
              <img
                alt="Man"
                src="../assets/avatar.webp"
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

            <!-- Dropdown menu -->
            <div id="dropdownHover" class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">
                <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownHoverButton">
                  <li>
                    <span class="block px-4 py-2">
                      Halo {{ $store.state.dataLogin.user.firstName }} <br>
                      Token tersisa: {{ $store.state.tokenRem }}
                    </span>
                  </li>
                  <li>
                    <router-link 
                    class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                    :class="active == 'home' ? 'font-bold' : ''"
                    to="/"> Beranda </router-link>
                  </li>
                  <li>
                    <router-link 
                    class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                    :class="active == 'brief' ? 'font-bold' : ''"
                    to="/brief"> Brief Generator </router-link>
                  </li>
      
                  <li>
                    <router-link 
                    class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                    :class="active == 'rater' ? 'font-bold' : ''"
                    to="/rater"> Design Rater </router-link>
                  </li>
      
                  <li>
                    <router-link 
                    class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                    :class="active == 'payment' ? 'font-bold' : ''"
                    to="/payment"> Pembayaran </router-link>
                  </li>
      
                  <li>
                    <router-link 
                    class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                    :class="active == 'history' ? 'font-bold' : ''"
                    to="/history"> Riwayat </router-link>
                  </li>
                  <li>
                    <span @click="logout()" 
                      class="block px-4 py-2 text-zimored hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white cursor-pointer">
                      Keluar Akun
                    </span>
                  </li>
                </ul>
            </div>
          </div>
        </div>
      </div>
    </header>
</template>