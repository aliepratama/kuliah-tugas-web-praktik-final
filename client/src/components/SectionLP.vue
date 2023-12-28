<script>
import { mapGetters } from 'vuex'
export default {
    name: 'Section Landing Page',
    props: {
        data: Object,
    },
    computed: {
      ...mapGetters(['isLogin'])
    }
}
</script>
<template>
    <section :id="data.id">
      <div class="mx-auto max-w-screen-xl mt-0 px-4 py-8 sm:px-6 sm:py-12 lg:px-8 lg:py-16">
        <div class="grid grid-cols-1 gap-8 lg:grid-cols-2 lg:gap-16">
          <div class="relative h-64 overflow-hidden rounded-lg sm:h-80 lg:h-full" :class="data.left ? 'lg:order-last' : ''">
            <img
              alt="Section Image"
              :src="data.image"
              class="absolute inset-0 h-full w-full object-cover"
            />
          </div>
    
          <div class="lg:py-24">
            <h2 class="text-3xl font-bold sm:text-4xl">{{ data.heading }}</h2>
    
            <p class="mt-4 text-gray-600">{{ data.paragraph }}</p>
    
            <router-link
              :to="$store.getters.isLogin ? data.ctaRoute : '/register'"
              class="mt-8 inline-block rounded bg-zimored px-12 py-3 text-sm font-medium text-white transition hover:bg-zimored focus:outline-none focus:ring focus:ring-zimoyellow"
            >
            {{ data.cta }}
            </router-link>
          </div>
        </div>
      </div>
    </section>
</template>