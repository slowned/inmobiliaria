<template>
  <v-container>
    <h1> Propiedades en alquiler </h1>
    <v-row justify="end">
      <v-col
        cols="12"
        sm="3"
      >
        <v-select
            :items="order"
            label="Ordenar por"
            dense
          ></v-select>
      </v-col>
    </v-row>
    <v-row>
      <v-dialog
        v-model="dialog"

        max-width="600px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="#846D34"
            dark
            fixed
            right
            fab
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-magnify</v-icon>
          </v-btn>
        </template>
          <SearchForm />
      </v-dialog>
    </v-row>
    <v-row>
        <v-row>
          <v-col cols="12" md="4" v-for="property in properties" :key="property.id">
            <PropertyList :property="property" />
          </v-col>
        </v-row>
    </v-row>

  </v-container>
</template>

<script>
import PropertyList from "@/components/PropertyList.vue";
import SearchForm from "@/components/SearchForm";
import PropertyService from "@/services/PropertyService.js";

export default {
  name: "Properties",
  components: {
    PropertyList,
    SearchForm,
  },
  data() {
    return {
      properties: null,
      dialog: false,
      order: ['Mas caro', 'Mas barato', 'Publicacion mas reciente', 'Publicacion mas antigua'],
    };
  },
  created() {
    PropertyService.getProperties()
      .then((response) => {
        this.properties = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    filterProperties(queryParams) {
      console.log('lo params viteh', queryParams);
      PropertyService.filterProperties(queryParams)
        .then((response) => {
          this.properties = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    reset() {
      this.$refs.form.reset()
    },

  },
};
</script>
