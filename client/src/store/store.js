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
        detailHistory: null,
        checkoutPage: 0,
        activePlan: null,
        imgQris: null,
        pricelist:[
          {
            id: 1,
            name: 'Bronze',
            token: 5,
            subtotal: 3500,
            tax: 350,
            discount: 350,
            total: 3500,
          },
          {
            id: 2,
            name: 'Silver',
            token: 10,
            subtotal: 5000,
            tax: 500,
            discount: 500,
            total: 5000,
          },
          {
            id: 3,
            name: 'Gold',
            token: 15,
            subtotal: 7000,
            tax: 700,
            discount: 700,
            total: 7000,
          },
        ],
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
        router.push('/');
      },
      changeRoute(state, { route }){
        state.activeRoute = route;
      },
      resetStateHistory(state){
        state.detailHistory = null;
        state.resultBrief = null;
        state.urlUploadedImage = null;
        state.resultRater = null;
      },
      resetStatePayment(state){
        state.activePlan = null;
        state.imgQris = null;
      },
      lanjutStepPayment(state, plan=-1, isReset=false){
        if(plan >= 0){
          state.activePlan = plan;
        }
        if(isReset){
          state.activePlan = null;
        }
        state.checkoutPage = state.checkoutPage === 2 ? 0 : state.checkoutPage + 1;
      },
      backStepPayment(state, isReset=false){
        if(isReset){
          state.activePlan = null;
        }
        state.checkoutPage = state.checkoutPage !== 0 ? state.checkoutPage - 1 : 0;
      },
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
              router.push('/').then(() => {router.go()});
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
        async actionBrief({ state, dispatch }, { type }){
          return await axios.post(`${defaultApi.toolsHost}/brief`, {
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
              state.resultBrief = Object.entries(res.data.data[0]);
              dispatch('actionGetToken');
              return true
            }else{
              alert('Gagal');
            }
          }).catch(async(error) => {
            let response = await error;
            // console.log(response)
            alert(response.response.data.errors)
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
        async actionRater({ state, dispatch }, { image }){
          return await axios.postForm(`${defaultApi.toolsHost}/rater`, {
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
              dispatch('actionGetToken');
              return true
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
          state.historyDataList = await HistoryDatabaseService.getAllData(state.dataLogin.user.id);
        },
        deleteHistory({ state }, { node }){
          HistoryDatabaseService.removeData(state.dataLogin.user.id, node);
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
        },
        async detailHistory({ state }, { node }){
          const data = await HistoryDatabaseService.detailData(state.dataLogin.user.id, node);
          console.log(data)
          state.detailHistory = data.tools;
          if (data.tools === 'rater'){
            state.urlUploadedImage = data.image_link;
            state.resultRater = Object.entries(data.result);
          } else{
            state.resultBrief = Object.entries(data.result);
          }
        },
        async actionPayment({ state, dispatch }, { planId }){
          return await axios.postForm(`${defaultApi.toolsHost}/payment/create`, {
            plan_id: planId
          },
          {
            timeout: 30000,
            headers: { 
              'Authorization': `Bearer ${state.dataLogin.token}`,
          }}).then((res) => {
            console.log(res)
            if(res.status == 200){
              // console.log(res)
              const data = res.data.data
              state.imgQris = data[0].qr_url;
              return true
            }else{
              alert('Gagal');
            }
          }).catch(async(error) => {
            let response = await error;
            // console.log(error)
            alert(response.response.data.errors)
          });
        },
    },
  })
