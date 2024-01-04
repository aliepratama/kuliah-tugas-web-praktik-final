<script>
import LoginForm from '../components/LoginForm.vue';
import Footer from '../components/Footer.vue';

export default {
  name: "Login Screen",
  components: {
    'LoginForm': LoginForm,
    'Footer': Footer,
  },
}
</script>

<template>
  <div class="w-full flex flex-col">
    <LoginForm class="w-full md:w-2/3"/>
    <Footer class="w-full mt-8"></Footer>
  </div>
</template>
