<template>
  <div class="flex w-full h-screen">
    <!-- Left Side - Hero Image and Text -->
    <div class="w-1/2 bg-gray-100 flex items-center justify-center" style="background-image: url('../assets/hero-image.jpg'); background-size: cover;">
      <div>
        <h1 class="text-4xl font-bold mb-4">Join the professional network you've been waiting for!</h1>
        <p class="text-lg">Our mission is to empower professionals worldwide by connecting them with the people, resources, and opportunities needed to succeed in their careers!</p>
      </div>
    </div>

    <!-- Right Side - Sign Up Form -->
    <div class="w-1/2 flex items-center justify-center">
      <div class="w-full max-w-md">
        <h2 class="text-3xl font-bold mb-6">SIGN UP</h2>
        <div class="mb-4">
          <label class="block text-sm font-medium mb-1">Create your profile!</label>
          <input type="text" class="form-input w-full"/>
        </div>
        <div class="mb-6">
          <button class="w-full py-2 px-4 bg-blue-500 text-white font-bold rounded hover:bg-blue-700">🎉 We’re holding peerlist.io/sankhaip10 for you!</button>
        </div>
        <div class="mb-6">
          <button class="w-full py-2 px-4 bg-gray-300 hover:bg-gray-400 rounded">Continue with email</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginComponent"
};
</script>

<style scoped>
.form-input {
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 0.25rem;
  width: 100%;
}
</style>
