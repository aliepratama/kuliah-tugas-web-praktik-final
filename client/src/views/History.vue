<script>
import { mapMutations } from 'vuex';
import HistoryListCard from '../components/HistoryListCard.vue';

export default {
    name: "History View",
    components:{
        'ListCard': HistoryListCard,
    },
    data(){
        return {
        }
    },
    methods: {
        ...mapMutations(['changeRoute']),
    },
    mounted(){
        this.$store.commit('changeRoute', { route: 'history' });
    }
}
</script>
<template>
    <div>
        <div class="w-full flex flex-col items-center p-10">
            <strong class="text-3xl font-bold text-gray-900 sm:text-4xl">Riwayat Layanan</strong>
            <ListCard></ListCard>
        </div>
    </div>
</template>