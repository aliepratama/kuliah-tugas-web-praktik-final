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
        <ListCard></ListCard>
    </div>
</template>