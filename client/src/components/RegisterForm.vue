<script>
import { mapActions, mapMutations, mapState } from 'vuex'
export default {
    name: 'Register Form',
    data(){
        return {
          ...mapState(['dataRegister']),
          firstName: null,
          lastName: null,
          email: null,
          password: null,
          passwordConfirm: null,
          agreement: false,
          lastPath: null,
        }
    },
    methods: {
      ...mapMutations(['checkRegister']),
      ...mapActions(['actionRegister']),
      register(){
        this.$store.commit('checkRegister', {
          firstName: this.firstName,
          lastName: this.lastName,
          email: this.email,
          password: this.password,
          passwordConfirm: this.passwordConfirm,
          agreement: this.agreement,
        })
        if(this.$store.state.dataRegister.accepted){
          this.$store.dispatch('actionRegister', {
            firstName: this.firstName,
            lastName: this.lastName,
            email: this.email,
            password: this.password,
          });
        } else{
          alert(this.$store.state.dataRegister.message);
        }
      },
    },
    created () {
      this.lastPath = this.$router.options.history.state.back
    },
    computed: {
      prevRoutePatch () {
        return this.lastPath ? this.lastPath : '/'
      }
    },
}
</script>
<template>
    <section class="bg-white">
      <div class="lg:grid lg:min-h-screen lg:grid-cols-12">
        <section class="relative flex h-32 items-end bg-gray-900 lg:col-span-5 lg:h-full xl:col-span-6">
          <img
            alt="Background for Register"
            src="https://images.unsplash.com/photo-1691144605799-cfaf2b18aa04?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHx0b3BpYy1mZWVkfDIxfENEd3V3WEpBYkV3fHxlbnwwfHx8fHw%3D&auto=format&fit=crop&w=870&q=80"
            class="absolute inset-0 h-full w-full object-cover opacity-80"
          />
    
          <div class="hidden lg:relative lg:block lg:p-12">
            <router-link class="block text-white" to="/">
              <span class="sr-only">Home</span>
              <img src="../assets/icon-white.webp" class="h-8 sm:h-10" alt="Logo Zimo White">
            </router-link>
    
            <h2 class="mt-6 text-2xl font-bold text-white sm:text-3xl md:text-4xl">
              Bergabung dengan Zimo
            </h2>
    
            <p class="mt-4 leading-relaxed text-white/90">
              Daftar untuk mendapatkan 5 token gratis dan menggunakan layanan eksklusif dari zimo tools
            </p>
          </div>
        </section>
    
        <main
          class="flex items-center justify-center px-8 py-8 sm:px-12 lg:col-span-7 lg:px-16 lg:py-12 xl:col-span-6"
        >
          <div class="max-w-xl lg:max-w-3xl">
            <div class="relative -mt-16 block lg:hidden">
              <router-link
                class="inline-flex h-16 w-16 items-center justify-center rounded-full bg-white text-zimored sm:h-20 sm:w-20"
                to="/"
              >
                <span class="sr-only">Home</span>
                <img src="../assets/icon.webp" class="h-8 sm:h-10" alt="Logo Zimo Color">
              </router-link>
    
              <h1 class="mt-2 text-2xl font-bold text-gray-900 sm:text-3xl md:text-4xl">
                Bergabung dengan Zimo
              </h1>
    
              <p class="mt-4 leading-relaxed text-gray-500">
                Daftar untuk mendapatkan 5 token gratis dan menggunakan layanan eksklusif dari zimo tools
              </p>
            </div>
    
            <router-link 
              :to="prevRoutePatch"
              class="text-sm text-gray-500 underline">
              Back
            </router-link>
            <form action="" class="mt-8 grid grid-cols-6 gap-6" autocomplete="off">
              <div class="col-span-6 sm:col-span-3">
                <label for="FirstName" class="block text-sm font-medium text-gray-700">
                  Nama depan
                </label>
    
                <input
                  type="text"
                  id="FirstName"
                  name="first_name"
                  v-model="firstName"
                  class="mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
                />
              </div>
    
              <div class="col-span-6 sm:col-span-3">
                <label for="LastName" class="block text-sm font-medium text-gray-700">
                  Nama belakang
                </label>
    
                <input
                  type="text"
                  id="LastName"
                  name="last_name"
                  v-model="lastName"
                  class="mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
                />
              </div>
    
              <div class="col-span-6">
                <label for="Email" class="block text-sm font-medium text-gray-700"> Email </label>
    
                <input
                  type="email"
                  id="Email"
                  name="email"
                  v-model="email"
                  class="mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
                />
              </div>
    
              <div class="col-span-6 sm:col-span-3">
                <label for="Password" class="block text-sm font-medium text-gray-700"> Kata sandi </label>
    
                <input
                  type="password"
                  id="Password"
                  name="password"
                  v-model="password"
                  class="mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
                />
              </div>
    
              <div class="col-span-6 sm:col-span-3">
                <label for="PasswordConfirmation" class="block text-sm font-medium text-gray-700">
                  Ulangi kata sandi
                </label>
    
                <input
                  type="password"
                  id="PasswordConfirmation"
                  name="password_confirmation"
                  v-model="passwordConfirm"
                  class="mt-1 w-full rounded-md border-gray-200 bg-white text-sm text-gray-700 shadow-sm"
                />
              </div>
    
              <div class="col-span-6">
                <label for="MarketingAccept" class="flex gap-4">
                  <input
                    type="checkbox"
                    id="MarketingAccept"
                    name="marketing_accept"
                    v-model="agreement"
                    :checked="agreement"
                    class="h-5 w-5 rounded-md border-gray-200 bg-white shadow-sm"
                  />
    
                  <span class="text-sm text-gray-700">
                    Saya setuju dengan syarat & ketentuan yang berlaku
                  </span>
                </label>
              </div>
    
              <div class="col-span-6 sm:flex sm:items-center sm:gap-4">
                <button
                  @click.prevent="register()"
                  class="inline-block shrink-0 rounded-md border border-zimored bg-zimored px-12 py-3 text-sm font-medium text-white transition hover:bg-transparent hover:text-zimored focus:outline-none focus:ring active:text-teal-500"
                >
                  Buat akun
                </button>
    
                <p class="mt-4 text-sm text-gray-500 sm:mt-0">
                  Sudah memiliki akun?
                  <router-link to="/login" class="text-gray-700 underline">Masuk</router-link>.
                </p>
              </div>
            </form>
          </div>
        </main>
      </div>
    </section>
  </template>