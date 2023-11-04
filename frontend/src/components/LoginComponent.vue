<template>
  <div class="flex min-h-screen bg-gray-100">
    <!-- Bind the backgroundImage style to a computed property or data property -->
    <div class="flex-1 flex justify-center items-center bg-cover" :style="backgroundImageStyle">
      <!-- You can add more images or text here -->
    </div>
    <!-- The rest of your template -->
  </div>
</template>

<script>
export default {
  name: 'LoginComponent',
  data() {
    return {
      // Assuming your image is located at src/assets/hero.png
      heroImage: require('@/assets/hero.png')
    };
  },
  computed: {
    backgroundImageStyle() {
      return {
        backgroundImage: `url(${this.heroImage})`
      };
    }
  }
};
</script>



<style scoped>
/* You can add additional styles here */
</style>
