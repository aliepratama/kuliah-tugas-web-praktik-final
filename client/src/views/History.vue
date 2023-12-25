<script>
import { mapActions, mapState } from 'vuex';
import NavBarLogin from '../components/NavBarLogin.vue';

export default {
    name: "History View",
    components:{
        'NavBarLogin': NavBarLogin,
    },
    data(){
        return {
            ...mapState(['historyDataList']),
        }
    },
    methods:{
        ...mapActions(['fetchAllHistory']),
    },
    mounted(){
        this.$store.dispatch('fetchAllHistory');
    },
}
</script>
<template>
    <div>
        <NavBarLogin active="history"></NavBarLogin>
        <p>{{ $store.state.historyDataList }}</p>
    </div>
</template>