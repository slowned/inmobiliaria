<template>
  <div class="home">
    <PropertyList v-for="property in properties" :key="property.id" :property="property" />
  </div>
</template>

<script>
// @ is an alias to /src
import PropertyList from "@/components/PropertyList.vue";
import PropertyService from "@/services/PropertyService.js";

export default {
  name: "Properties",
  components: {
    PropertyList,
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
