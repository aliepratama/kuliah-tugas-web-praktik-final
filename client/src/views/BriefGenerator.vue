<script>
import { mapActions, mapState } from 'vuex';
import NavBarLogin from '../components/NavBarLogin.vue';

export default {
  name: "Brief Generator View",
  components:{
    'NavBarLogin': NavBarLogin,
  },
  data(){
    return {
      ...mapState(['resultBrief']),
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
                v-model="selectModel"
              >
                <option value="">Silahkan pilih...</option>
                <option v-for="select in selection" :key="select" :value="select.value">{{ select.name }}</option>
              </select>
            </div>
            <button
              class="block w-full rounded bg-teal-600 px-12 py-3 text-sm font-medium text-white shadow hover:bg-teal-600 focus:outline-none focus:ring active:bg-teal-600 sm:w-auto"
              @click="$store.dispatch('actionBrief', {type: selectModel})"
            >
              Generate!
            </button>
          </div>
        </div>
        <div class="w-full flex justify-center">
          <div class="overflow-x-auto w-2/3">
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
          </div>
        </div>
    </div>
</template>