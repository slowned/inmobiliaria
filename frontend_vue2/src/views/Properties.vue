<template>
  <v-container>
    <h2> Propiedades en alquiler </h2>
    <v-row>
      <v-col cols="12" md="8">
        <v-row>
          <v-col cols="12" md="4" v-for="property in properties" :key="property.id">
            <PropertyList :property="property" />
          </v-col>
        </v-row>
      </v-col>

      <v-col cols="12" md="4">
        <h3> Buscar por </h3>
        <SearchForm />
      </v-col>
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
};
</script>
