<script>
import RegisterForm from '../components/RegisterForm.vue';
import Footer from '../components/Footer.vue';

export default {
  name: "Register Screen",
  components: {
    'RegisterForm': RegisterForm,
    'Footer': Footer,
  },
}
</script>

<template>
  <div class="w-full flex flex-col">
    <RegisterForm class="w-full"/>
    <Footer class="w-full mt-8"></Footer>
  </div>
</template>
