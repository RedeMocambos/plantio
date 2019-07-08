<template>
    <v-container fluid>
        <v-layout>
            <v-flex
                xs10
                offset-xs1
            >
                <v-data-table
                    :headers="header"
                    :items="especies"
                >
                    <template
                        v-slot:items="props"
                    >
                        <td>{{ props.index + 1 }}</td>
                        <td>
                            <v-btn
                                flat
                                small
                                @click="visualizar(props.item.id)"
                            >
                                <v-icon class="pr-2">
                                    local_florist
                                </v-icon>
                                {{ props.item.nome_cientifico }}
                            </v-btn>
                        </td>
                        <td>{{ props.item.familia }}</td>
                        <td>{{ props.item.nomes_populares }}</td>
                        <td>
                            <v-btn
                                flat
                                small
                                @click="editar(props.item.id)"
                            >
                                <v-icon class="pr-2">
                                    edit
                                </v-icon>
                                editar
                            </v-btn>
                            <v-btn
                                flat
                                small
                                @click="excluir(props.item.id)"
                            >
                                <v-icon class="pr-2">
                                    clear
                                </v-icon>
                                excluir
                            </v-btn>
                        </td>
                    </template>
                </v-data-table>
                <v-btn
                    dark
                    class="green darken-1"
                    @click="adicionar()"
                >
                    <v-icon
                        white
                        class="pr-2">
                        add
                    </v-icon>
                    adicionar especie
                </v-btn>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'Especies',
    data() {
        return {
            header: [
                {
                    text: '#',
                    align: 'left',
                    sortable: false,
                    value: 'numero',
                },
                {
                    align: 'center',
                    text: 'nome científico',
                    value: 'nome_cientifico',
                },
                {
                    align: 'center',
                    text: 'família',
                    value: 'familia',
                },
                {
                    align: 'center',
                    text: 'nomes populares',
                    value: 'nomes_populares',
                },
                {
                    align: 'center',
                    text: 'ações',
                    value: 'acoes',
                },
            ],
            especies: [],
        };
    },
    computed: {
        ...mapGetters({
            listaEspecies: 'especie/especies',
        }),
    },
    watch: {
        listaEspecies() {
            this.especies = this.listaEspecies;
        },
    },
    created() {
        this.buscarEspecies();
    },
    methods: {
        ...mapActions({
            buscarEspecies: 'especie/buscarEspecies',
            adicionarEspecie: 'especie/adicionarEspecie',
        }),
        visualizar(id) {
            const path = `/especie/${id}`;
            this.$router.push({ path });
        },
        editar(id) {
            const path = `/especie/${id}/editar`;
            this.$router.push({ path });
        },
        adicionar() {
            const path = `/especie/criar`;
            this.$router.push({ path });
        },
        excluir(id) {
        },
    },
};
</script>
