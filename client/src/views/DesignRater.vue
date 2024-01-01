<script>
import { mapActions, mapMutations, mapState } from 'vuex';
import Stepper from '../components/Stepper.vue';
import ResultRater from '../components/ResultRater.vue';

export default {
  name: "Design Rater View",
  components:{
    'Stepper': Stepper,
    'ResultRater': ResultRater,
  },
  methods : {
    ...mapActions(['actionImageUploader', 'actionRater']),
    ...mapMutations(['changeRoute']),
    async uploadDroppedFiles($event) {
      const image = $event.dataTransfer.items[0].getAsFile();
      this.$store.dispatch('actionImageUploader', {image: image});
      this.lanjutStep();
    },
    uploadInputtedFiles($event){
      const image = $event.target.files[0];
      this.$store.dispatch('actionImageUploader', {image: image});
      this.lanjutStep();
    },
    rateImage(){
      this.$store.dispatch('actionRater', {
        image: this.$store.state.urlUploadedImage});
        this.lanjutStep();
    },
    lanjutStep(){
      this.activeStep = this.activeStep === 4 ? 1 : this.activeStep + 1;
    },
    backStep(){
      this.activeStep = this.activeStep !== 1 ? this.activeStep - 1 : 1;
    },
  },
  data() {
    return {
      ...mapState(['urlUploadedImage']),
      dataStepper: [
        {
          id: 1,
          name: 'Info',
        },
        {
          id: 2,
          name: 'Upload',
        },
        {
          id: 3,
          name: 'Konfirmasi',
        },
        {
          id: 4,
          name: 'Hasil',
        },
      ],
      activeStep: 1,
    };
  },
  mounted(){
    this.$store.commit('changeRoute', { route: 'rater' });
  }
};
</script>
<template>
  <div class="w-full flex flex-col items-center py-4 px-2">
      <div class="w-full flex justify-center gap-4 items-center">
        <span v-if="activeStep > 1" @click="backStep()" class="text-sm text-gray-500 underline cursor-pointer">
          Kembali
        </span>
        <div class="w-full md:w-3/4 lg:w-1/2">
          <Stepper :datalists="dataStepper" :active="activeStep"/>
        </div>
      </div>
      <transition name="fade">
        <div v-if="activeStep == 1" class="w-full flex flex-col items-center gap-8">
          <div class="h-64 overflow-hidden rounded-lg aspect-auto">
            <img
              alt="Brief Generator Illustration"
              src="https://i.ibb.co/fn6gWLS/section2.webp"
              class="inset-0 h-full w-full object-cover"
            />
          </div>
          <div class="w-full flex flex-col items-center gap-2">
            <strong class="text-3xl font-bold text-gray-900 sm:text-4xl">
              Nilai desain logo anda otomatis!
            </strong>
            <p class="sm:text-xl/relaxed">
              Lihat apakah desain anda sesuai kriteria dengan kecanggihan AI
            </p>
          </div>
          <button
              @click="lanjutStep()"
              class="block w-full rounded bg-zimored px-12 py-3 text-sm font-medium text-white shadow hover:bg-zimored focus:outline-none focus:ring active:bg-zimored sm:w-auto"
            >
              Lanjut
          </button>
        </div>
        <div v-else-if="activeStep == 2" class="w-full flex flex-col items-center gap-8 py-8">
          <h5 class="text-3xl font-bold text-gray-900 sm:text-4xl">
                  Silahkan upload desain
          </h5>
          <div 
            class="flex items-center justify-center w-full px-2 lg:w-2/3"
            @dragover.prevent @drop.prevent="uploadDroppedFiles"
            >
              <label for="dropzone-file" class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                  <div class="flex flex-col items-center justify-center pt-5 pb-6">
                      <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                      </svg>
                      <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Klik untuk unggah</span> atau drag and drop</p>
                      <p class="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG or GIF (MAX. 800x400px)</p>
                  </div>
                  <input id="dropzone-file" type="file" class="hidden" @change.prevent="uploadInputtedFiles"/>
              </label>
          </div> 
        </div>
        <div v-else-if="activeStep == 3" class="w-full flex flex-col items-center gap-8 py-8">
          <h5 class="text-3xl font-bold text-gray-900 sm:text-4xl">
                  Konfirmasi desain
          </h5>
          <div class="flex flex-col items-center w-full gap-y-4">
              <img :src="$store.state.urlUploadedImage" class="w-1/3 aspect-auto" alt="result_form">
              <button @click="rateImage()" class="block w-full rounded bg-zimored px-12 py-3 text-sm font-medium text-white shadow hover:bg-zimored focus:outline-none focus:ring active:bg-zimored sm:w-auto">Kirim</button>
          </div>
        </div>
        <div v-else class="w-full flex justify-center">
          <div class="overflow-x-auto w-2/3 md:w-1/2 flex flex-col items-center gap-8 py-8">
            <ResultRater></ResultRater>
            <button
              class="block w-full rounded bg-zimored px-12 py-3 text-sm font-medium text-white shadow hover:bg-zimored focus:outline-none focus:ring active:bg-zimored sm:w-auto"
              @click="lanjutStep()"
            >
              Buat lagi!
            </button>
          </div>
        </div>
      </transition>
  </div>
</template>