<script>
import NavBar from './components/NavBar.vue';
import NavBarLogin from './components/NavBarLogin.vue';
import { mapGetters, mapState } from 'vuex';

export default {
  name: 'Home Screen',
  components: {
    'NavBarLogin': NavBarLogin,
    'NavBar': NavBar,
  },
  data(){
    return {
      ...mapState(['activeRoute']),
    }
  },
  computed: {
    ...mapGetters(['isLogin'])
  }
}
</script>

<template>
  <div>
    <NavBarLogin 
      v-if="$store.getters.isLogin"
      :active="$store.state.activeRoute"
    />
    <NavBar v-else/>
    <router-view v-slot="{ Component }">
      <transition name="fade">
        <component :is="Component"/>
      </transition>
    </router-view>
  </div>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.25s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.fade-enter-active{
  transition-delay: 0.3s;
}
</style>