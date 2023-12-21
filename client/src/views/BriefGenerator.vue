<script>
import NavBarLogin from '../components/NavBarLogin.vue';

export default {
  name: "Brief Generator Page",
  components:{
    'NavBarLogin': NavBarLogin,
  },
  data(){
    return {
      selection: ['Logo', 'Web Design'],
      result: null,
    }
  },
  methods:{
    kirim(){

    }
  },
};
</script>
<template>
    <div>
        <NavBarLogin active="brief"></NavBarLogin>
        <div class="w-full flex justify-center">
          <div class="w-3/4 py-10 flex flex-col items-center gap-y-4">
            <div>
              <label for="HeadlineAct" class="block text-sm font-medium text-gray-900">Silahkan pilih mode generator</label>
            
              <select
                name="HeadlineAct"
                id="HeadlineAct"
                class="mt-1.5 w-full rounded-lg border-gray-300 text-gray-700 sm:text-sm"
              >
                <option value="">Silahkan pilih...</option>
                <option v-for="select in selection" :key="select" :value="select">{{ select }}</option>
              </select>
            </div>
            <button
              class="block w-full rounded bg-teal-600 px-12 py-3 text-sm font-medium text-white shadow hover:bg-teal-600 focus:outline-none focus:ring active:bg-teal-600 sm:w-auto"
              @click="kirim()"
            >
              Generate!
            </button>
          </div>
        </div>
        <p>{{ result }}</p>
    </div>
</template>