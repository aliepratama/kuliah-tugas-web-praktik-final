<script>
import Header from '../components/Header.vue';
import Footer from '../components/Footer.vue';
import SectionLP from '../components/SectionLP.vue';
import { mapMutations } from 'vuex';

export default {
  name: 'Home Screen',
  components: {
    'Header': Header,
    'Footer': Footer,
    'SectionLP': SectionLP,
  },
  data() {
    return {
      sectionData: [
        {
          id: 'brief',
          heading: 'Buat brief desain otomatis!',
          image: 'https://i.ibb.co/tJPMfvb/section1.webp',
          paragraph: 'Dengan bantuan AI, Anda dapat meningkatkan skill desain dari banyak studi kasus yang diberikan. Hasil brief yang dihasilkan unik sehingga Anda tidak perlu khawatir untuk projek yang duplikat.',
          cta: 'Coba Brief Generator',
          ctaRoute: '/brief',
          left: true,
        },
        {
          id: 'rater',
          heading: 'Ketahui skor desain anda!',
          image: 'https://i.ibb.co/fn6gWLS/section2.webp',
          paragraph: 'Setelah menghasilkan rancangan desain, Anda dapat meminta AI untuk membantu proses penilaian dengan kriteria desain yang professional dan cocok untuk customer.',
          cta: 'Coba Design Rater',
          ctaRoute: '/rater',
          left: false,
        },
        {
          id: 'pricing',
          heading: 'Harga terjangkau!',
          image: 'https://i.ibb.co/yQj8bRd/section3.webp',
          paragraph: 'Harga paket token yang sangat murah dapat membantu menaikkan skill anda. Pembayaran mudah hanya dengan scan QRIS dan beberapa sentuhan saja!',
          cta: 'Lihat pembayaran',
          ctaRoute: '/payment',
          left: true,
        },
      ],
    }
  },
  methods: {
    ...mapMutations(['changeRoute']),
  },
  mounted(){
    this.$store.commit('changeRoute', { route: 'home' });
  },
}
</script>

<template>
  <div>
    <Header></Header>
    <SectionLP v-for="section in sectionData" :key="section.id" :data="section"/>
    <Footer></Footer>
  </div>
</template>
