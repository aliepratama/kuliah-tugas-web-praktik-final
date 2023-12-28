<script>
import { mapActions, mapState } from 'vuex';
export default {
    name: 'History List Card',
    data(){
        return {
            ...mapState(['historyDataList']),
        }
    },
    computed: {
        historyList(){
            try{
                const data = Object.values(this.$store.state.historyDataList);
                return data;
            } catch (e){
                
            }
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
        <p>{{ historyList }}</p>
        <ul class="mt-4 space-y-2">
            <li>
                <a href="#" class="block h-full rounded-lg border border-gray-700 p-4 hover:border-pink-600">
                    <strong class="font-medium text-white">Project A</strong>
    
                    <p class="mt-1 text-xs font-medium text-gray-300">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime consequuntur deleniti,
                    unde ab ut in!
                    </p>
                </a>
            </li>
            <li>
                <a href="#" class="block h-full rounded-lg border border-gray-700 p-4 hover:border-pink-600">
                    <strong class="font-medium text-white">Project A</strong>
    
                    <p class="mt-1 text-xs font-medium text-gray-300">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime consequuntur deleniti,
                    unde ab ut in!
                    </p>
                </a>
            </li>
        </ul>
    </div>
</template>