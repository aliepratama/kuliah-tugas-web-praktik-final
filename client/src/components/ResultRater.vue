<script>
import { mapState } from 'vuex'

export default {
    name: 'Result Rater',
    data(){
        return {
            ...mapState(['urlUploadedImage', 'resultRater']),
        }
    },
}
</script>
<template>
    <div class="flex flex-col md:flex-row justify-center items-center w-full gap-8 py-8">
        <img :src="$store.state.urlUploadedImage" class="w-full max-w-xs aspect-auto" alt="result_form">
        <table class="divide-y-2 divide-gray-200 bg-white text-sm">
            <thead class="ltr:text-left">
                <tr>
                <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900">Kriteria</th>
                <th class="px-4 py-2 font-medium text-gray-900">Hasil</th>
                </tr>
            </thead>
        
            <tbody class="divide-y divide-gray-200">
                <tr v-for="result in $store.state.resultRater" :key="result[0]">
                <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center">{{ result[0] }}</td>
                <td class="px-4 py-2 text-gray-700 text-center">
                    <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    class="h-5 w-5 text-green-500"
                    v-if="result[1]"
                    >
                    <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                    </svg>
                    <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    class="h-5 w-5 text-zimored"
                    v-else
                    >
                    <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                    </svg>
                </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>