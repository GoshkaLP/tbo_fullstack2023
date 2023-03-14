import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

let url = "http://localhost:8082"

export default new Vuex.Store({
  state: {
    locations: [],
    federalLocations: [],
    federalsInfo: []
  },
  getters: {
    getLocations(state) {
      return state.locations;
    },
    getFederalLocations(state) {
      return state.federalLocations;
    },
    getFederalsInfo(state) {
      return state.federalsInfo;
    }
  },
  mutations: {
    setLocations(state, payload) {
      state.locations = payload;
    },
    setFederalLocations(state, payload) {
      state.federalLocations = payload;
    },
    setFederalsInfo(state, payload) {
      state.federalsInfo = payload;
    }
  },
  actions: {
    async fetchLocations(state) {
      const response = await axios.get(url + "/api/locations");
      state.commit('setLocations', response.data.data);
    },
    async fetchFederalSubjectsLocations(state) {
      const response = await axios.get(url + "/api/federalSubjectsLocations")
      state.commit("setFederalLocations", response.data.data);
    },
    async fetchFederalsInfo(state) {
      const response =  await axios.get(url + "/api/federalSubjects")
      state.commit("setFederalsInfo", response.data.data)
    }
  },
  modules: {
  }
})
