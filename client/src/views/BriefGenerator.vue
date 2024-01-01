<script>
import { mapActions, mapMutations, mapState } from 'vuex';
import ResultBrief from '../components/ResultBrief.vue';
import Stepper from '../components/Stepper.vue';

export default {
  name: "Brief Generator View",
  components:{
    'Stepper': Stepper,
    'ResultBrief': ResultBrief,
  },
  data(){
    return {
      dataStepper: [
        {
          id: 1,
          name: 'Info',
        },
        {
          id: 2,
          name: 'Pilih tipe',
        },
        {
          id: 3,
          name: 'Hasil',
        },
      ],
      activeStep: 1,
      selection: [
      {
        'name': 'Logo',
        'value': 'logo',
      },
      {
        'name': 'Web Design',
        'value': 'website',
      },
      ],
      selectModel: '',
    }
  },
  methods:{
    ...mapActions(['actionBrief']),
    ...mapMutations(['changeRoute']),
    lanjutStep(){
      this.activeStep = this.activeStep === 3 ? 1 : this.activeStep + 1;
    },
    backStep(){
      this.activeStep = this.activeStep !== 1 ? this.activeStep - 1 : 1;
    },
  },
  mounted(){
    this.$store.commit('changeRoute', { route: 'brief' });
  },
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
                src="https://i.ibb.co/tJPMfvb/section1.webp"
                class="inset-0 h-full w-full object-cover"
              />
            </div>
            <div class="w-full flex flex-col items-center gap-2">
              <strong class="text-3xl font-bold text-gray-900 sm:text-4xl">
                Buat Brief desain otomatis!
              </strong>
              <p class="sm:text-xl/relaxed">
                Mulai buat brief dengan kecanggihan AI
              </p>
            </div>
            <button
                @click="lanjutStep()"
                class="block w-full rounded bg-zimored px-12 py-3 text-sm font-medium text-white shadow hover:bg-zimored focus:outline-none focus:ring active:bg-zimored sm:w-auto"
              >
                Lanjut
            </button>
          </div>
          <div v-else-if="activeStep == 2" class="w-full flex justify-center">
            <div class="w-3/4 py-10 flex flex-col items-center gap-8">
              <div class="w-full flex flex-col items-center gap-8">
                <label for="HeadlineAct" class="text-3xl font-bold text-gray-900 sm:text-4xl">
                  Silahkan pilih mode generator
                </label>
              
                <select
                  name="HeadlineAct"
                  id="HeadlineAct"
                  class="w-full md:w-1/2 rounded-lg border-gray-300 text-gray-700 sm:text-sm"
                  v-model="selectModel"
                >
                  <option value="">Silahkan pilih...</option>
                  <option v-for="select in selection" :key="select" :value="select.value">{{ select.name }}</option>
                </select>
              </div>
              <button
                class="block w-full rounded bg-zimored px-12 py-3 text-sm font-medium text-white shadow hover:bg-zimored focus:outline-none focus:ring active:bg-zimored sm:w-auto"
                @click="$store.dispatch('actionBrief', {type: selectModel}); lanjutStep()"
              >
                Generate!
              </button>
            </div>
          </div>
          <div v-else class="w-full flex justify-center">
            <div class="overflow-x-auto w-2/3 flex flex-col items-center gap-8 py-8">
              <ResultBrief></ResultBrief>
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