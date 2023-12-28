<script>
export default {
    name: 'NavBar',
    data(){
        return {

        }
    }
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
                  <a class="text-gray-500 transition hover:text-gray-500/75" href="/#brief"> Brief Generator </a>
                </li>
    
                <li>
                  <a class="text-gray-500 transition hover:text-gray-500/75" href="/#rater"> Design Rater </a>
                </li>
    
                <li>
                  <a class="text-gray-500 transition hover:text-gray-500/75" href="/#pricing"> Pembayaran </a>
                </li>
    
              </ul>
            </nav>
          </div>
    
          <div class="flex items-center gap-4">
            <div class="sm:flex sm:gap-4">
              <router-link
                class="rounded-md bg-zimored px-5 py-2.5 text-sm font-medium text-white shadow"
                to="/login"
              >
                Masuk
              </router-link>
    
              <div class="hidden sm:flex">
                <router-link
                  class="rounded-md bg-gray-100 px-5 py-2.5 text-sm font-medium text-zimored"
                  to="/register"
                >
                  Daftar
                </router-link>
              </div>
            </div>
    
            <div class="block md:hidden">
              <button class="rounded bg-gray-100 p-2 text-gray-600 transition hover:text-gray-600/75">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    </header>
</template>