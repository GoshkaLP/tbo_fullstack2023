import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

let url = "http://localhost:8082"

export default new Vuex.Store({
  state: {
    locations: [],
    federalLocations: [],
    federalsInfo: [],
    locationInfo: {
      isLoaded: false,
      data: []
    }
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
    },
    getLocationInfo(state) {
      return state.locationInfo.data;
    },
    getLocationInfoStatus(state) {
      return state.locationInfo.isLoaded;
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
    },
    setLocationInfo(state, payload) {
      state.locationInfo.data = payload;
    },
    setLocationInfoStatus(state, payload) {
      state.locationInfo.isLoaded = payload;
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
    },
    async fetchLocationInfo(state, objId) {
      state.commit('setLocationInfoStatus', false);
      const response = await axios.get(url + '/api/locationsInfo/' + objId)
      state.commit("setLocationInfo", response.data.data)
      state.commit("setLocationInfoStatus", true);
    }
  },
  modules: {
  }
})
