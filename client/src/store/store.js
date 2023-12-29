import { createStore } from 'vuex'
import { router } from '../router/router'
import { defaultApi } from './config';
import axios from 'axios';
import { HistoryDatabaseService } from '../services/HistoryDataService';

export const store = createStore({
    state(){
      return {
        dataRegister: {
          accepted: false
        },
        dataLogin: {
          user: window.localStorage.getItem('user') ? JSON.parse(window.localStorage.getItem('user')) : null,
          token: window.localStorage.getItem('token'),
        },
        resultBrief: null,
        urlUploadedImage: null,
        resultRater: null,
        historyDataList: null,
        pricingState: 'pricing',
        tokenRem: 0,
        activeRoute: 'home',
      }
    },
    getters: {
      isLogin(state){
        return state.dataLogin.user && state.dataLogin.token;
      },
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
      changeRoute(state, { route }){
        state.activeRoute = route;
      },
      // changeStepPayment(state){
      //   if 
      // },
    },
    actions: {
        actionLogin({ state }, { email, password }){
          axios.postForm(`${defaultApi.toolsHost}/auth/login`, {
            email: email, password: password
          }).then((res) => {
            if(res.status == 200){
              // console.log(res.data.data[0])
              let result = res.data.data[0];
              window.localStorage.setItem('user', JSON.stringify({
                id: result.id,
                firstName: result.first_name,
                email: result.email,
              }));
              window.localStorage.setItem('token', result.access_token);
              state.dataLogin.id = result.id;
              state.dataLogin.token = result.access_token;
              state.dataLogin.firstName = result.first_name;
              router.push('/');
            }else{
              alert('Gagal');
            }
          }).catch(async(error) => {
            let response = await error.response.data.errors;
            // console.log(response)
            alert(response)
          });
        },
        actionRegister(context, { firstName, lastName, email, password }){
          axios.postForm(`${defaultApi.toolsHost}/account`, {
            email: email, password: password, firstName: firstName, lastName: lastName
          }).then((res) => {
            if(res.status == 200){
              console.log(res.data.data[0]);
              alert('Berhasil Mendaftar!');
              router.push('/login');
            }
          }).catch(async(error) => {
            let response = await error.response.data.errors;
            // console.log(response)
            alert(response)
          });
        },
        actionBrief({ state }, { type }){
          console.log({
            type: type,
            bearer: state.dataLogin.token
          })
          axios.post(`${defaultApi.toolsHost}/brief`, {
            type: type
          },{
            timeout: 30000,
            headers: { 
              'Authorization': `Bearer ${state.dataLogin.token}`,
              'Content-Type': 'application/json',
            }
          }).then((res) => {
            if(res.status == 200){
              // console.log(res.data.data[0])
              state.resultBrief = Object.entries(res.data.data[0])
            }else{
              alert('Gagal');
            }
          }).catch(async(error) => {
            let response = await error.response.data.errors;
            // console.log(response)
            alert(response)
          });
        },
        actionImageUploader({ state }, { image }){
          axios.postForm(`https://api.imgbb.com/1/upload?expiration=15552000&key=${defaultApi.imgbbKey}`,
          {image: image}).then((res) => {
            // console.log(res.data)
            state.urlUploadedImage = res.data.data.display_url;
          }).catch(async(error) => {
            let response = await error.response.data.errors;
            alert(response)
          });
        },
        actionRater({ state }, { image }){
          axios.postForm(`${defaultApi.toolsHost}/rater`, {
            img_url: image
          },
          {
            timeout: 30000,
            headers: { 
              'Authorization': `Bearer ${state.dataLogin.token}`,
          }}).then((res) => {
            if(res.status == 200){
              // console.log(res.data.data)
              const data = res.data.data
              state.resultRater = Object.entries(data[0]);
            }else{
              alert('Gagal');
            }
          }).catch(async(error) => {
            let response = await error.response.data.errors;
            // console.log(response)
            alert(response)
          });
        },
        async fetchAllHistory({ state }){
          state.historyDataList = await HistoryDatabaseService.getAllData()
        },
        actionGetToken({ state }){
          axios.get(`${defaultApi.toolsHost}/account/${state.dataLogin.user.id}`,
          {
            timeout: 30000,
            headers: { 
              'Authorization': `Bearer ${state.dataLogin.token}`,
          }}).then((res) => {
            if(res.status == 200){
              // console.log(res.data.data)
              state.tokenRem = res.data.data[0].token
            }else{
              alert('Gagal');
            }
          }).catch(async(error) => {
            let response = await error.response.data.errors;
            // console.log(response)
            alert(response)
          });
        }
    },
  })
