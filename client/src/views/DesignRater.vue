<script>
import { mapActions, mapMutations, mapState } from 'vuex';
export default {
  name: "Design Rater View",
  components:{
  },
  methods : {
    ...mapActions(['actionImageUploader', 'actionRater']),
    ...mapMutations(['changeRoute']),
    async uploadDroppedFiles($event) {
      const image = $event.dataTransfer.items[0].getAsFile();
      this.$store.dispatch('actionImageUploader', {image: image});
    },
    uploadInputtedFiles($event){
      const image = $event.target.files[0];
      this.$store.dispatch('actionImageUploader', {image: image});
    },
    rateImage(){
      this.$store.dispatch('actionRater', {
        image: this.$store.state.urlUploadedImage});
    }
  },
  data() {
    return {
      ...mapState(['urlUploadedImage', 'resultRater']),
    };
  },
  mounted(){
    this.$store.commit('changeRoute', { route: 'rater' });
  }
};
</script>
<template>
    <div>
      <div 
        class="flex items-center justify-center w-full"
        @dragover.prevent @drop.prevent="uploadDroppedFiles"
        v-if="!$store.state.urlUploadedImage">
          <label for="dropzone-file" class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
              <div class="flex flex-col items-center justify-center pt-5 pb-6">
                  <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                  </svg>
                  <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop</p>
                  <p class="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG or GIF (MAX. 800x400px)</p>
              </div>
              <input id="dropzone-file" type="file" class="hidden" @change.prevent="uploadInputtedFiles"/>
          </label>
      </div> 
      <div v-else class="flex flex-col items-center w-full gap-y-4">
        <img :src="$store.state.urlUploadedImage" class="w-1/3 aspect-auto" alt="result_form">
        <button @click="rateImage()" class="block w-full rounded bg-zimored px-12 py-3 text-sm font-medium text-white shadow hover:bg-zimored focus:outline-none focus:ring active:bg-zimored sm:w-auto">Kirim</button>
        <p>{{ $store.state.resultRater }}</p>
      </div>
    </div>
</template>