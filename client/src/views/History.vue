<script>
import { mapMutations, mapState } from 'vuex';
import HistoryListCard from '../components/HistoryListCard.vue';
import ResultBrief from '../components/ResultBrief.vue';
import ResultRater from '../components/ResultRater.vue';
import Footer from '../components/Footer.vue';

export default {
    name: "History View",
    components:{
        'ListCard': HistoryListCard,
        'ResultBrief': ResultBrief,
        'ResultRater': ResultRater,
        'Footer': Footer,
    },
    data(){
        return {
            ...mapState(['detailHistory']),
        }
    },
    methods: {
        ...mapMutations(['changeRoute', 'resetStateHistory']),
    },
    mounted(){
        this.$store.commit('changeRoute', { route: 'history' });
    }
}
</script>
<template>
    <div>
        <div class="w-full flex flex-col items-center p-10">
            <div class="w-full flex justify-center items-center gap-4">
                <span v-if="$store.state.detailHistory" @click="resetStateHistory()" class="text-sm text-gray-500 underline cursor-pointer">
                    Kembali
                </span>
                <strong class="text-3xl font-bold text-gray-900 sm:text-4xl">Riwayat Layanan</strong>
            </div>
            <transition name="fade">
                <Suspense v-if="$store.state.detailHistory === 'brief'"><ResultBrief class="mt-4 w-full px-16"></ResultBrief></Suspense>
                <Suspense v-else-if="$store.state.detailHistory === 'rater'"><ResultRater class="mt-4"></ResultRater></Suspense>
                <ListCard v-else></ListCard>
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