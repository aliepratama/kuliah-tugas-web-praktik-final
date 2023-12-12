import { createStore } from 'vuex'
import { router } from '../router/router'
import { defaultApi } from './config';
import axios from 'axios';

export const store = createStore({
    state(){
      return {
        dataRegister: {
          accepted: false
        },
        dataLogin: {
          'id': window.localStorage.getItem('id'),
          'token': window.localStorage.getItem('token')
        },
      }
    },
    getters: {
      isLogin(state){
        return state.dataLogin.id && state.dataLogin.token
      }
    },
    mutations: {
      checkRegister(state, { firstName, lastName, email,
        password, passwordConfirm, agreement }){
         if(firstName && email && password && passwordConfirm && agreement){
          if(password.length > 6 && password === passwordConfirm){
            state.dataRegister = {
              accepted: true,
              message: 'Berhasil!',
              data: { firstName: firstName, lastName: lastName,
                email: email, password: password },
            };
          } else {
            state.dataRegister.message = 'Password tidak valid!';
          }
         }else {
           state.dataRegister.message = 'Mohon lengkapi data!';
         }
      },
      actionLogout(state){
        window.localStorage.removeItem('id');
        window.localStorage.removeItem('token');
        state.dataLogin.id = null;
        state.dataLogin.token = null;
      },
    },
    actions: {
        actionLogin({ state }, { email, password }){
          axios.postForm(`${defaultApi.toolsHost}/auth/login`, {
            email: email, password: password
          }).then((res) => {
            if(res.status == 200){
              console.log(res.data.data[0])
              let result = res.data.data[0];
              window.localStorage.setItem('id', result.id);
              window.localStorage.setItem('token', result.access_token);
              state.dataLogin.id = result.id;
              state.dataLogin.token = result.access_token;
              router.push('/');
            }else{
              alert('Gagal');
            }
          }).catch(async(error) => {
            let response = await error.response.data.errors;
            console.log(response)
            alert(response)
          });
        },
        actionRegister(context, { firstName, lastName, email, password }){
          console.log('Pendaftaran')
        }
    },
  })
