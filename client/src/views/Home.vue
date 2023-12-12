<script>
import NavBar from '../components/NavBar.vue';
import NavBarLogin from '../components/NavBarLogin.vue';
import Header from '../components/Header.vue';
import Footer from '../components/Footer.vue';
import { mapGetters } from 'vuex';

export default {
  name: 'Home Screen',
  components: {
    'NavBarLogin': NavBarLogin,
    'NavBar': NavBar,
    'Header': Header,
    'Footer': Footer,
  },
  computed: {
    ...mapGetters(['isLogin'])
  }
}
</script>

<template>
  <div>
    <NavBarLogin v-if="isLogin"/>
    <NavBar v-else/>
    <Header></Header>
    <Footer></Footer>
  </div>
</template>
