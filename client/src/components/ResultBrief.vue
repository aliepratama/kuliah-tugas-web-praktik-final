<script>
import { mapState, useStore } from 'vuex'
export default {
    name: 'Result Brief',
    props: {
        type: String,
    },
    data(){
        return {
            ...mapState(['resultBrief']),
        }
    },
    async setup(props){
        const store = useStore();
        const typeForm = props.type;
        if(store.state.detailHistory !== 'brief'){
            const data = await store.dispatch('actionBrief', {
                    type: typeForm})
            return {data: data}
        }
        return {}
    },
}
</script>
<template>
    <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
        <thead class="ltr:text-left">
            <tr>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Subjek</th>
            <th class="px-4 py-2 font-medium text-gray-900">Poin</th>
            </tr>
        </thead>

        <tbody class="divide-y divide-gray-200">
            <tr v-for="result in $store.state.resultBrief" :key="result[0]">
            <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">{{ result[0] }}</td>
            <td class="px-4 py-2 text-gray-700">{{ result[1] }}</td>
            </tr>
        </tbody>
    </table>
</template>