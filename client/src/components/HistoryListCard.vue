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
                const data = Object.entries(this.$store.state.historyDataList);
                data.sort((a, b) => a[1].timestamp - b[1].timestamp);
                return data;
            } catch (e){
                
            }
        }
    },
    methods:{
        ...mapActions(['fetchAllHistory']),
        categoryMethod(tools, type){
            if(tools === 'brief'){
                if(type === 'logo'){
                    return 'Logo Brief';
                }
                return 'Web Design Brief';
            }
            return 'Design Rate';
        },
        timestampToString(timestamp){
            return new Date(timestamp * 1000).toLocaleDateString()
        },
    },
    mounted(){
        this.$store.dispatch('fetchAllHistory');
    },
}
</script>
<template>
    <div class="w-full">
        <div class="w-full flex justify-center">
            <ul class="w-full grid grid-cols-1 gap-y-4 gap-x-4 md:grid-cols-2 lg:gap-y-0 lg:grid-cols-3 px-4 py-8 sm:px-6 sm:py-12 lg:px-8 lg:py-16">
                <li v-for="[key, history] in historyList" :key="key">
                    <div class="p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
                        <svg v-if="history.tools == 'brief'" class="w-7 h-7 text-gray-500 dark:text-gray-400 mb-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 576 512">
                            <path d="M249.6 471.5c10.8 3.8 22.4-4.1 22.4-15.5V78.6c0-4.2-1.6-8.4-5-11C247.4 52 202.4 32 144 32C93.5 32 46.3 45.3 18.1 56.1C6.8 60.5 0 71.7 0 83.8V454.1c0 11.9 12.8 20.2 24.1 16.5C55.6 460.1 105.5 448 144 448c33.9 0 79 14 105.6 23.5zm76.8 0C353 462 398.1 448 432 448c38.5 0 88.4 12.1 119.9 22.6c11.3 3.8 24.1-4.6 24.1-16.5V83.8c0-12.1-6.8-23.3-18.1-27.6C529.7 45.3 482.5 32 432 32c-58.4 0-103.4 20-123 35.6c-3.3 2.6-5 6.8-5 11V456c0 11.4 11.7 19.3 22.4 15.5z"/>
                        </svg>
                        <svg v-else class="w-7 h-7 text-gray-500 dark:text-gray-400 mb-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 576 512">
                            <path d="M316.9 18C311.6 7 300.4 0 288.1 0s-23.4 7-28.8 18L195 150.3 51.4 171.5c-12 1.8-22 10.2-25.7 21.7s-.7 24.2 7.9 32.7L137.8 329 113.2 474.7c-2 12 3 24.2 12.9 31.3s23 8 33.8 2.3l128.3-68.5 128.3 68.5c10.8 5.7 23.9 4.9 33.8-2.3s14.9-19.3 12.9-31.3L438.5 329 542.7 225.9c8.6-8.5 11.7-21.2 7.9-32.7s-13.7-19.9-25.7-21.7L381.2 150.3 316.9 18z"/>
                        </svg>
                        <h5 class="mb-2 text-2xl font-semibold tracking-tight text-gray-900 dark:text-white">{{ categoryMethod(history.tools, history.type) }}</h5>
                        <p class="mb-3 font-normal text-gray-500 dark:text-gray-400">Tanggal aktivitas: {{ timestampToString(history.timestamp) }}</p>
                        <a href="#" class="inline-flex items-center text-zimored hover:underline">
                            Lihat Detail
                            <svg class="w-3 h-3 ms-2.5 rtl:rotate-[270deg]" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11v4.833A1.166 1.166 0 0 1 13.833 17H2.167A1.167 1.167 0 0 1 1 15.833V4.167A1.166 1.166 0 0 1 2.167 3h4.618m4.447-2H17v5.768M9.111 8.889l7.778-7.778"/>
                            </svg>
                        </a>
                    </div>
                </li>
            </ul>
        </div>
        <!-- <p>{{ historyList }}</p> -->
    </div>
</template>