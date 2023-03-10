import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    locations: []
  },
  getters: {
    getLocations(state) {
      return state.locations;
    }
  },
  mutations: {
    setLocations(state, payload) {
      state.locations = payload;
    }
  },
  actions: {
    async fetchLocations(state) {
      const response = await axios.post("http://localhost:8082/api/locations");
      state.commit('setLocations', response.data.data);
    }
  },
  modules: {
  }
})
