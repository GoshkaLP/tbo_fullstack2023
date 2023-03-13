import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

let url = "http://localhost:8082"

export default new Vuex.Store({
  state: {
    locations: [],
    federalLocations: []
  },
  getters: {
    getLocations(state) {
      return state.locations;
    },
    getFederalLocations(state) {
      return state.federalLocations;
    }
  },
  mutations: {
    setLocations(state, payload) {
      state.locations = payload;
    },
    setFederalLocations(state, payload) {
      state.federalLocations = payload;
    }
  },
  actions: {
    async fetchLocations(state) {
      const response = await axios.post(url + "/api/locations");
      state.commit('setLocations', response.data.data);
    },
    async fetchFederalSubjectsLocations(state) {
      const response = await axios.get(url + "/api/federalSubjectsLocations")
      state.commit("setFederalLocations", response.data.data);
    }
  },
  modules: {
  }
})
