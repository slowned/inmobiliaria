<template>
  <v-container>
      <v-card
        class="mx-auto"
        max-width="400"
      >
        <v-img
          class="white--text align-end"
          height="200px"
          src="https://picsum.photos/350/165?random"
        >
          <v-card-title>{{ property.address }}</v-card-title>
        </v-img>

        <v-card-subtitle class="pb-0">
          precio $: {{ property.price }}
        </v-card-subtitle>

        <v-card-text class="text--primary">
          <div>
            {{ property.description }}
          </div>
        </v-card-text>

        <v-divider class="mx-4"></v-divider>

        <v-card-title>
          Servicios
        </v-card-title>

        <v-card-actions>
          <v-btn
            color="orange"
            text
            :to="{ name: 'PropertyDetail', params: { id: property.id } }"
          >
            Conocer
          </v-btn>
        </v-card-actions>
      </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'propertyList',
  props: {
    property: Object
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
