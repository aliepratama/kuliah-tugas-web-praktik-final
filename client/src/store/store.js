import { createStore } from 'vuex'
import { router } from '../router/router'

export const store = createStore({
    state(){
      return {
        isLogin: window.localStorage.getItem('isLogin'),
      }
    },
    mutations: {
      successLogin(state){
        state.isLogin = true;
        window.localStorage.setItem('isLogin', state.isLogin);
    },
    successLogout(state){
        state.isLogin = false;
        window.localStorage.removeItem('isLogin');
      },
    },
    actions: {
        forceSuccessLogin({ commit }){
            commit('successLogin');
            router.push('/')
        },
        forceSuccessLogout({ commit }){
            commit('successLogout');
            router.go()
        }
    },
  })
