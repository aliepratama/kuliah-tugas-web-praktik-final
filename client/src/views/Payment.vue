<script>
import Pricing from '../components/Pricing.vue';
import Checkout from '../components/Checkout.vue';
import Payment from '../components/Payment.vue';
import Spinner from '../components/Spinner.vue';
import Footer from '../components/Footer.vue';
import { mapMutations, mapState } from 'vuex';

export default {
    name: "Payment View",
    components:{
        'Pricing': Pricing,
        'Checkout': Checkout,
        'Payment': Payment,
        'Spinner': Spinner,
        'Footer': Footer,
    },
    data(){
        return {
            ...mapState(['checkoutPage', 'activePlan']),
        }
    },
    methods: {
        ...mapMutations(['changeRoute']),
    },
    mounted(){
        this.$store.commit('changeRoute', { route: 'payment' });
    }
}
</script>
<template>
    <div>
        <div class="flex flex-col items-center py-10">
            <strong class="text-3xl font-bold text-gray-900 sm:text-4xl">Pembelian Paket</strong>
            <transition name="fade">
                <Pricing v-if="$store.state.checkoutPage === 0"></Pricing>
                <Checkout v-else-if="$store.state.checkoutPage === 1"></Checkout>
                <suspense v-else>
                    <template #default>
                        <Payment></Payment>
                    </template>
                    <template #fallback>
                        <Spinner></Spinner>
                    </template>
                </suspense>
            </transition>
            <Footer class="w-full mt-8"></Footer>
        </div>
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