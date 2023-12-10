<script setup>
import { ref } from 'vue';
import NavBar from '../components/NavBar.vue';
import NavBarLogin from '../components/NavBarLogin.vue';
import Header from '../components/Header.vue';
import Footer from '../components/Footer.vue';
import { store } from '../store/store';

const isLogin = ref(store.state.isLogin);
</script>

<template>
  <div>
    <NavBarLogin v-if="isLogin"/>
    <NavBar v-else/>
    <Header></Header>
    <Footer></Footer>
  </div>
</template>
