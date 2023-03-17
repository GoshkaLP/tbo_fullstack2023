<template>
  <div>
    <div id="chart">
      <b-card>
        <apexchart type="bar" height="350" :options="getChartOptions" :series="getSeries"></apexchart>
      </b-card>
    </div>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
import {mapActions, mapGetters} from "vuex";
export default {
  name: "AnalyticsView",
  components: {
    apexchart: VueApexCharts
  },
  data() {
    return {

    }
  },
  methods: {
    ...mapActions(['fetchFundingSportTypes']),
  },
  computed: {
    ...mapGetters(['getFundingSportTypes']),
    getChartOptions() {
      return {
        chart: {
          type: 'bar',
          height: 500,
          stacked: true,
          toolbar: {
            show: true
          },
          zoom: {
            enabled: true
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
              position: 'bottom',
              offsetX: -10,
              offsetY: 0
            }
          }
        }],
        plotOptions: {
          bar: {
            horizontal: false,
            borderRadius: 10,
            dataLabels: {
              total: {
                enabled: true,
                style: {
                  fontSize: '13px',
                  fontWeight: 900
                }
              }
            }
          },
        },
        xaxis: {
          type: 'category',
          categories: this.getFundingSportTypes.categories,
        },
        legend: {
          position: 'right',
          offsetY: 40
        },
        fill: {
          opacity: 1
        },
        dataLabels: {
          enabled: false,
        },
      }
    },
    getSeries() {
      return this.getFundingSportTypes.series;
    }
  },
  created() {
    this.fetchFundingSportTypes();
  }

}
</script>

<style scoped>

</style>