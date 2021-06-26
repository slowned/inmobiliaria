<template>
  <v-container>
    <h2> Propiedades en alquiler </h2>
    <v-card-text style="height: 100px; position: absolute" class="d-md-none">
      <v-fab-transition>
        <v-btn

        color="#846D34"
        dark
        fixed
        right
        fab
        @click="dialog = !dialog"
        >
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
    </v-fab-transition>
  </v-card-text>
  <v-dialog
    v-model="dialog"
    max-width="500px"
  >
    <SearchForm />
  </v-dialog>
    <v-row>
      <v-col cols="12" md="8">
        <v-row>
          <v-col cols="12" md="4" v-for="property in properties" :key="property.id">
            <PropertyList :property="property" />
          </v-col>
        </v-row>
      </v-col>

      <v-col cols="12" md="4" class="hidden-xs-only">
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
      hidden: true,
      dialog: false,
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
