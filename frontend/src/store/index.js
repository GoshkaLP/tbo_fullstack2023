import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

let url = "https://tbo.gmrybkin.com"

export default new Vuex.Store({
  state: {
    locations: [],
    federalLocations: [],
    hexagonLocations: [],
    federalsInfo: [],
    locationInfo: {
      isLoaded: false,
      data: {
        info: [],
        spending: [],
        supervisory: []
      }
    },
    fundingSportTypes: {},
    constructionSportTypes: {}
  },
  getters: {
    getLocations(state) {
      return state.locations;
    },
    getFederalLocations(state) {
      return state.federalLocations;
    },
    getHexagonLocations(state) {
      return state.hexagonLocations;
    },
    getFederalsInfo(state) {
      return state.federalsInfo;
    },
    getLocationInfo(state) {
      return state.locationInfo.data;
    },
    getLocationInfoStatus(state) {
      return state.locationInfo.isLoaded;
    },
    getFundingSportTypes(state) {
      return state.fundingSportTypes;
    },
    getConstructionSportTypes(state) {
      return state.constructionSportTypes;
    }
  },
  mutations: {
    setLocations(state, payload) {
      state.locations = payload;
    },
    setFederalLocations(state, payload) {
      state.federalLocations = payload;
    },
    setHexagonLocations(state, payload) {
      state.hexagonLocations = payload;
    },
    setFederalsInfo(state, payload) {
      state.federalsInfo = payload;
    },
    setLocationInfo(state, payload) {
      state.locationInfo.data.info = payload.info;
      state.locationInfo.data.spending = payload.spending;
      state.locationInfo.data.supervisory = payload.supervisory;
    },
    setLocationInfoStatus(state, payload) {
      state.locationInfo.isLoaded = payload;
    },
    setFundingSportTypes(state, payload) {
      state.fundingSportTypes = payload
    },
    setConstructionSportTypes(state, payload) {
      state.constructionSportTypes = payload
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
    async fetchHexagonLocations(state) {
      const response = await axios.get(url + "/api/hexagonLocations")
      state.commit("setHexagonLocations", response.data.data);
    },
    async fetchFederalsInfo(state) {
      const response =  await axios.get(url + "/api/federalSubjects")
      state.commit("setFederalsInfo", response.data.data)
    },
    async fetchLocationInfo(state, objId) {
      state.commit('setLocationInfoStatus', false);
      const response = await axios.get(url + '/api/location/' + objId)
      state.commit("setLocationInfo", response.data.data)
      state.commit("setLocationInfoStatus", true);
    },
    async fetchFundingSportTypes(state) {
      const response = await axios.get(url + '/api/fundingSportTypes')
      state.commit("setFundingSportTypes", response.data.data)
    },
    async fetchConstructionSportTypes(state) {
      const response = await axios.get(url + '/api/constructionSportTypes')
      state.commit("setConstructionSportTypes", response.data.data)
    }

  },
  modules: {
  }
})
